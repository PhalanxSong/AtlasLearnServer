function getMongoUrl() {
	if (process.env.MONGO_DB_URI) {
		return MONGO_DB_URI;
	} else if (process.env.MONGO_PORT_27017_TCP_ADDR) {
		return `mongodb://${process.env.MONGO_PORT_27017_TCP_ADDR}:${process.env.MONGO_PORT_27017_TCP_PORT}/phalanx-asset-server`;
	} else {
		return 'mongodb://localhost/phalanx-asset-server';
	}
}

const config = {
	environment: process.env.NODE_ENV || 'dev',
	server: {
		address: process.env.TSM_SERVER_HOST || 'http://localhost',
		port: process.env.TSM_SERVER_PORT || 8010
	},
	mongo: {
		url: getMongoUrl(),
		port: process.env.MONGO_PORT_27017_TCP_PORT || 27017,
		host: process.env.MONGO_PORT_27017_TCP_ADDR || 'localhost',
		adminUsername: process.env.TSM_MONGO_CLIENT_USERNAME || 'admin',
		adminPassword: process.env.TSM_MONGO_CLIENT_PASSWORD || 'pass'
	},
	needAuth: process.env.TSM_NEED_AUTH === undefined || process.env.TSM_NEED_AUTH === true || process.env.TSM_NEED_AUTH === 'true',
	jwtSecret: process.env.TSM_JWT_SECRET || 'lunatic'
};

module.exports = config;