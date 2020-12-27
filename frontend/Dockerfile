ARG APP_NAME=app
FROM node:15.5.0 as builder
ARG APP_NAME
ENV APP $APP_NAME

RUN mkdir $APP
WORKDIR $APP

COPY package.json package-lock.json ./

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
## RUN npm ci && mkdir /ng-app && mv ./node_modules ./ng-app
RUN npm ci

# Copying the code to APP directory
COPY . .

## Build the angular app in production mode and store the artifacts in dist folder
RUN npm run ng build -- --prod --output-path=dist


FROM nginx:1.19.6-alpine
RUN apk add --no-cache bash
ARG APP_NAME
ENV APP $APP_NAME

EXPOSE 8081
## Copy our default nginx config which will replace the existing default.conf
COPY default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From ‘builder’ stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder $APP/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
