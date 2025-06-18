import { spawnSync } from "child_process";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

export function runBrowserTask(task: string, model: string = "gpt-3.5-turbo"): void {
  const script = join(
    dirname(fileURLToPath(import.meta.url)),
    "../../browser/browser_agent.py",
  );
  const result = spawnSync("python3", [script, model, task], {
    stdio: "inherit",
  });
  if (result.error) {
    throw result.error;
  }
}
