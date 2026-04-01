import { describe, expect, it } from "vitest";

describe("CI smoke test", () => {
    it("runs a basic assertion", () => {
        expect(true).toBe(true);
    });
});
