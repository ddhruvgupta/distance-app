# Use an official Node.js image as the base image
FROM node:20-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy only package.json and package-lock.json to leverage Docker caching
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Use an official Nginx image to serve the built app
FROM nginx:alpine

# Copy the built React app to the Nginx HTML directory
COPY --from=build /app/build /usr/share/nginx/html
COPY public/config.js /usr/share/nginx/html/config.js

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["sh", "-c", "envsubst < /usr/share/nginx/html/config.js > /usr/share/nginx/html/config.js && nginx -g 'daemon off;'"]