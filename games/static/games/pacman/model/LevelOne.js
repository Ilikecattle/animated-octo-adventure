(function() {

var LevelOne = function() {
	this.map = [

	['gp', 'g', 'gR', 'g', 'g', 'g*', 'g', 'g', 'gR', 'g', 'g', 'g', 'gR'],
	['g', 'g', 'gR', 'g', 'g', 'g', 'g', 'g', 'gR', 'g', 'g', 'g', 'gR'],
	['g', 'g', 'gR', 'g', 'g', 'g', 'g', 'g', 'gR', 'g', 'g', 'g', 'g*'],
	['g', 'g', 'g*', 'g', 'g', 'gR', 'g', 'g', 'g*', 'g', 'g', 'g', 'g*'],
	['g', 'g', 'g', 'g', 'g', 'gR', 'g', 'g', 'g', 'g', 'g', 'g', 'gR'],
	['g', 'g', 'g', 'g', 'g', 'gR', 'g', 'g', 'g', 'g', 'g', 'g', 'gR'],

	];
}

var p = LevelOne.prototype = new Level();

this.LevelOne = LevelOne;

}());