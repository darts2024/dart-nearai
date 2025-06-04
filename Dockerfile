FROM  oven/bun AS builder
WORKDIR /app


COPY package.json bun.lock ./

RUN bun install


# Deploy stage
FROM oven/bun

ENV NODE_ENV="production"
ENV OUTPUT_DIR="/outputs/"
ENV Prompt='minimalistic polygon geometric car in brutalism warehouse'
ENV RANDOM_SEED=40


RUN mkdir -p /outputs

WORKDIR /app


COPY . .

COPY --from=builder /app/node_modules ./node_modules
# RUN bun run build
# CMD ["sh", "-c", "npm run test && npm run test:e2e"]

ENTRYPOINT ["bun", "start"]

CMD [ "generate" ]

LABEL maintainer="Hiro <laciferin@gmail.com>"
