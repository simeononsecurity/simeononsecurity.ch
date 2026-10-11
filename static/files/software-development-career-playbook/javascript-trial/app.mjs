const METERS_TO_FEET = 3.28084;

export function convertMetersToFeet(rawValue) {
  const meters = Number(rawValue);
  if (!Number.isFinite(meters) || meters < 0) {
    throw new Error("meters must be a finite, nonnegative number");
  }
  return (meters * METERS_TO_FEET).toFixed(2);
}

if (process.argv[1] === new URL(import.meta.url).pathname) {
  const rawValue = process.argv[2];
  if (rawValue === undefined || rawValue === "--help") {
    console.log("Usage: node app.mjs METERS");
    process.exit(rawValue === "--help" ? 0 : 2);
  }
  try {
    console.log(`${rawValue} meters = ${convertMetersToFeet(rawValue)} feet`);
  } catch (error) {
    console.error(error.message);
    process.exit(2);
  }
}
