FROM node:18-alpine

WORKDIR /app

# 1) install only production deps
COPY package.json package-lock.json ./
RUN npm install --omit=dev

# 2) copy rest of your code
COPY . .

# 3) expose & run
EXPOSE 3000
CMD ["npm", "start"]
