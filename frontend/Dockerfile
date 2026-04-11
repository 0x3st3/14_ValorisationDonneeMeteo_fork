ARG NODE_BASE_IMAGE
FROM ${NODE_BASE_IMAGE}

WORKDIR /app

COPY package*.json .

RUN npm ci

COPY . .

RUN npm run build

ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=3000

EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]
