FROM  oven/bun AS builder
WORKDIR /app

# COPY package*.json pnpm-lock.yaml ./

COPY . .

# COPY .env.example .env

RUN bun install


# Deploy stage
FROM oven/bun

ENV NODE_ENV="production"
ENV OUTPUT_DIR="/outputs/"
ENV PROMPT='minimalistic polygon geometric car in brutalism warehouse'
ENV RANDOM_SEED=40


RUN mkdir -p /outputs

WORKDIR /app

COPY --from=builder /app .

# RUN bun run build
# CMD ["sh", "-c", "npm run test && npm run test:e2e"]

ENTRYPOINT ["bun", "start"]

CMD [ "generate" ]

LABEL maintainer="Hiro <laciferin@gmail.com>"
