(function(){
	
var RandomEnemyMover = function(game) {
	this.started = false;
	this.game = game;
}

var p = RandomEnemyMover.prototype;

p.start = function() {
	this.enemies = this.game.getEnemies();
	this.started = true;
}

p.stop = function() {
	this.started = false;
}

p.update = function() {
	if(!this.started)
		return;
	var enemy = this.getRandomEnemy();
	this.game.moveEnemy(enemy, this.getRandomDir());
}

p.getRandomEnemy = function() {
	if(this.enemies.length == 0)
		return;

	var enemyIndex = Math.random() * this.enemies.length;
	return this.enemies[parseInt(enemyIndex)];
}

p.getRandomDir = function() {
	var rand = Math.random();

	if(rand < 0.25) {
		return Dir.UP;
	} else if(rand < 0.5) {
		return Dir.DOWN;
	} else if(rand < 0.75) {
		return Dir.RIGHT;
	} else {
		return Dir.LEFT;
	}

}

this.RandomEnemyMover = RandomEnemyMover;

}());