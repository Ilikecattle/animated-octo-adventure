(function() {

var Game = function() {
    this.enemies = new Array();
}

p = Game.prototype;

p.getEnemies = function() {
    return this.enemies;
}

p.movePlayer = function(dir) {
    if(this.player == null)
        return;

    var targetTile = this.map.tileAtDirection(this.player.getTile(), dir);
    if(targetTile == null) {
        return;
    }
    var currentContent = targetTile.topSprite();
    if (this.tileCanBeAttacked(targetTile)) {
        this.attackEnemy(this.player, currentContent);
    }
    if(this.tileCanBeOccupied(targetTile)) {
        this.player.deoccupy();
        this.player.occupy(targetTile);
        this.player.setDirection(dir);
    }
    update();
}

p.moveEnemy = function(enemy, dir) {
    if(enemy == null)
        return;

    var targetTile = this.map.tileAtDirection(enemy.getTile(), dir);
    if(targetTile == null)
        return;
    if(this.tileCanBeOccupied(targetTile)) {
        var currentContent = targetTile.topSprite();
        if(currentContent == this.player) {
            console.log("DIE");
        }
        enemy.deoccupy();
        enemy.occupy(targetTile);
    }
    update();
}

p.attackEnemy = function(player, currentSprite) {
    var enemy = null;
    if(currentSprite.getSpriteType() == SpriteType.GHOST) {
        for(var i = 0; i < this.enemies.length; i++) {
            enemy = this.enemies[i];
            if(enemy == currentSprite) {
                enemy.deoccupy();
                this.enemies.splice(i, 1);
                break;
            }
        }
    }
}

p.tileCanBeOccupied = function(targetTile) {
    var currentOccupier = targetTile.topSprite();
    if(currentOccupier == null)
        return false;
    var spriteType = currentOccupier.getSpriteType();
    return spriteType != SpriteType.ROCK && spriteType != SpriteType.GHOST;
}

p.tileCanBeAttacked = function(targetTile) {
    return targetTile.containsSpriteType(SpriteType.GHOST);
}

p.addPlayer = function(p) {
    this.player = p;
}

p.addEnemy = function(e) {
    this.enemies.push(e);
}

p.getMap = function() {
    return this.map;
}

p.setMap = function(map) {
	this.map = map;
}

p.isRoomCleared = function() {
    return !this.getMap().containsEnemy();
}

this.Game = Game;

}());