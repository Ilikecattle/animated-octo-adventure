Bitmap.prototype.setWidth = function(w)
{
    if (this.image == null || this.image.width == 0) return;
    this.scaleX = w / this.image.width;
}

Bitmap.prototype.setHeight = function(h)
{
    if (this.image == null || this.image.height == 0) return;
    this.scaleY = h / this.image.height;
}

initialize = function() {
	stage = new createjs.Stage("demoCanvas");
	level = new LevelOne();
	game = createModel();
	createUI();
	stage.canvas.tabIndex = 1000;
	stage.canvas.style.outline = "none";
	Ticker.setFPS(5);
	Ticker.addEventListener("tick", function(event) {
		mapRenderer.render();
		enemyMover.update();
		stage.update();
	});
};

createModel = function() {
	return level.parseMap();
}

getGame = function() {
	return game;
}

createUI = function() {
	playerInteraction = new PlayerInteraction();
	playerInteraction.withGameInteractor(game);
	enemyMover = new RandomEnemyMover(getGame());
	playerInteraction.controlling(enemyMover);
	playerInputListener = new PlayerInputListener(playerInteraction);
	mapRenderer = new MapRenderer(game.getMap());
	stage.addChild(mapRenderer);
	playerInteraction.start();
}

update = function() {
    mapRenderer.render();
    stage.update();
    playerInteraction.updateState();
}