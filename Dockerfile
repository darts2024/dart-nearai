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
ENV OUTPUT_DIR="/outputs/"
ENV PROMPT='minimalistic plolygon geometric car in brutalism warehouse'


RUN mkdir -p /outputs

WORKDIR /app

RUN npm install -g bun # the other bun not visible here

COPY --from=builder /app ./

# RUN bun run build
# CMD ["sh", "-c", "npm run test && npm run test:e2e"]

ENTRYPOINT ["bun", "start"]

CMD [ "generate" ]

LABEL maintainer="Hiro <laciferin@gmail.com>"
