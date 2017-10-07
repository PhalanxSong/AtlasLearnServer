# 基于 node 镜像创建
FROM node

# 设置环境变量
ENV APP_HOME /app/
ENV TEMP_NPM /temp

# 执行命令
RUN mkdir $APP_HOME

# 设置容器启动命令
CMD [ "npm run start" ]

# 缓存 NPM 包
WORKDIR $TEMP_NPM
COPY package.json $TEMP_NPM
RUN npm config set registry https://registry.npm.taobao.org
RUN npm install
RUN cp -a $TEMP_NPM/node_modules $APP_HOME

# ???
WORKDIR $APP_HOME
COPY ./ $APP_HOME

# 可以不在此处声明
EXPOSE 8010
