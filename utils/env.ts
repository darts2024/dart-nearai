export function env<T>(key: string, defaultVal: T): T {
  const value = process.env[key];
  return (value !== undefined ? (value as unknown as T) : defaultVal);
}
