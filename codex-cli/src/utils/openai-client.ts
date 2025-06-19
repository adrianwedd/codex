import type { AppConfig } from "./config.js";

import {
  getBaseUrl,
  getApiKey,
  AZURE_OPENAI_API_VERSION,
  OPENAI_TIMEOUT_MS,
  OPENAI_ORGANIZATION,
  OPENAI_PROJECT,
} from "./config.js";
import { log } from "./logger/log.js";
import { wrapOpenAI } from "langsmith/wrappers/openai";
import OpenAI, { AzureOpenAI } from "openai";

type OpenAIClientConfig = {
  provider: string;
};

/**
 * Creates an OpenAI client instance based on the provided configuration.
 * Handles both standard OpenAI and Azure OpenAI configurations.
 *
 * @param config The configuration containing provider information
 * @returns An instance of either OpenAI or AzureOpenAI client
 */
export function createOpenAIClient(
  config: OpenAIClientConfig | AppConfig,
): OpenAI | AzureOpenAI {
  const headers: Record<string, string> = {};
  if (OPENAI_ORGANIZATION) {
    headers["OpenAI-Organization"] = OPENAI_ORGANIZATION;
  }
  if (OPENAI_PROJECT) {
    headers["OpenAI-Project"] = OPENAI_PROJECT;
  }

  let client: OpenAI | AzureOpenAI;
  if (config.provider?.toLowerCase() === "azure") {
    client = new AzureOpenAI({
      apiKey: getApiKey(config.provider),
      baseURL: getBaseUrl(config.provider),
      apiVersion: AZURE_OPENAI_API_VERSION,
      timeout: OPENAI_TIMEOUT_MS,
      defaultHeaders: headers,
    });
  } else {
    client = new OpenAI({
      apiKey: getApiKey(config.provider),
      baseURL: getBaseUrl(config.provider),
      timeout: OPENAI_TIMEOUT_MS,
      defaultHeaders: headers,
    });
  }

  if (
    process.env["LANGCHAIN_TRACING_V2"] === "true" ||
    process.env["LANGSMITH_TRACING_V2"] === "true"
  ) {
    try {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      client = wrapOpenAI(client as any);
    } catch (err) {
      log(`Failed to enable LangSmith tracing: ${String(err)}`);
    }
  }

  return client;
}
