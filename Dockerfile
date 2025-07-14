FROM  oven/bun:alpine AS builder
WORKDIR /app


COPY package.json bun.lock ./

COPY . .

RUN bun install

# BUN: so if u compile for alpine-> it will only work in alpine
RUN bun build --compile --minify ./index.ts --outfile nearai


# Deploy stage
FROM node:alpine

ENV NODE_ENV="production"
ENV OUTPUT_DIR="/outputs/"
ENV Prompt='minimalistic polygon geometric car in brutalism warehouse'
ENV RANDOM_SEED=40


RUN mkdir -p /outputs

WORKDIR /app

COPY --from=builder /app/nearai .

RUN chmod +x ./nearai

ENTRYPOINT ["./nearai"]

CMD [ "generate" ]

LABEL maintainer="Hiro <laciferin@gmail.com>"
