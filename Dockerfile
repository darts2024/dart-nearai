FROM  oven/bun AS builder
WORKDIR /app


COPY package.json bun.lock ./

COPY . .

RUN bun install

RUN bun build --compile --minify ./index.ts --outfile nearai


# Deploy stage
FROM alpine

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
