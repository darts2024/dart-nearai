FROM node:23 AS builder
WORKDIR /app

#COPY package*.json pnpm-lock.yaml ./

COPY . .

# COPY .env.example .env


RUN npm install -g bun
RUN bun install


# Deploy stage
FROM node:23-alpine

ENV NODE_ENV="production"

WORKDIR /app

RUN npm install -g bun # the other bun not visible here

COPY --from=builder /app ./

RUN bun run build
# CMD ["sh", "-c", "npm run test && npm run test:e2e"]

ENTRYPOINT ["bun", "run", "start"]

LABEL maintainer="Hiro <laciferin@gmail.com>"
