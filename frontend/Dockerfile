ARG NODE_BUILD_BASE_IMAGE
ARG NODE_RUNTIME_BASE_IMAGE

FROM ${NODE_BUILD_BASE_IMAGE} AS build

WORKDIR /app

COPY package*.json .
RUN ["npm", "ci"]

COPY . .
RUN ["npm", "run", "build"]

FROM ${NODE_RUNTIME_BASE_IMAGE}

WORKDIR /app

ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=3000

COPY --from=build /app/.output /app/.output
COPY --from=build /app/public /app/public

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
