import assert from "node:assert/strict";
import test from "node:test";

import { convertMetersToFeet } from "./app.mjs";

test("one meter", () => {
  assert.equal(convertMetersToFeet("1"), "3.28");
});

test("zero meters", () => {
  assert.equal(convertMetersToFeet("0"), "0.00");
});

test("decimal input", () => {
  assert.equal(convertMetersToFeet("2.5"), "8.20");
});

test("negative input is rejected", () => {
  assert.throws(() => convertMetersToFeet("-1"), /nonnegative/);
});

test("text input is rejected", () => {
  assert.throws(() => convertMetersToFeet("secret"), /finite/);
});
