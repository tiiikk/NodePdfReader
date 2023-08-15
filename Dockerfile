FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
