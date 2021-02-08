FROM node:10-alpine

WORKDIR /frontend

COPY . .

RUN npm install yarn
RUN yarn add
RUN yarn add create-react-app
RUN yarn add react-router-dom


ENTRYPOINT ["yarn"]
CMD ["start"]