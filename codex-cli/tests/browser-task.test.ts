import { describe, it, expect, vi } from "vitest";
import { runBrowserTask } from "../src/utils/browser-task.js";
import { spawnSync } from "child_process";

vi.mock("child_process", () => ({
  spawnSync: vi.fn(() => ({ status: 0 })),
}));

describe("runBrowserTask", () => {
  it("spawns python script", () => {
    runBrowserTask("test-task");
    expect(spawnSync).toHaveBeenCalled();
  });
});
