
FROM node

WORKDIR /project

COPY package*.json ./

RUN npm install
COPY . .

EXPOSE 8080
CMD [ "npm", "run", "serve" ]
