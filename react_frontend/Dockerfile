FROM node:13-alpine

WORKDIR /frontend

COPY . /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install --silent
RUN npm install react-scripts@3.3.1 -g --silent

CMD ["npm", "start"]