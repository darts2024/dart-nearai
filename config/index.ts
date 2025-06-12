import { env } from "@utils/env.ts"


export const IMAGE_PROMPT = env(
  "Prompt",
  "A wide cinematic anime scene of a glowing AI supercore suspended in a glass dome atop a mountain observatory at sunrise. Below, a futuristic city awakens — neon grid lines pulse through skyscrapers as drones and digital avatars fly between data towers. In the foreground, a young engineer with windswept hair and a long coat stands on a cliff, overlooking it all, holding a glowing cube (representing artificial intelligence). Light flares, sakura petals in the wind, vibrant sky gradients — in the style of Makoto Shinkai, hyper-detailed, emotional, majestic."
)

export const IMAGE_MODEL = env("IMAGE_MODEL", "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic")
