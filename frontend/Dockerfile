# Use an official Node image
FROM node:20-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json if exists
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy app code
COPY . .

# Expose Next.js port
EXPOSE 3000

# Run Next.js in development mode
CMD ["npm", "run", "dev"]
