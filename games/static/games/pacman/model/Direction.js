(function() {

var Direction = function( x, y ) {
	this.dx = x;
	this.dy = y;
}

	var p = Direction.prototype;

	p.getDx= function() {
		return this.dx;
	}

	p.getDy = function() {
		return this.dy;
	}

	p.toString = function() {
		return "Direction to string";
	}

	this.Direction = Direction;

}());

this.Dir = this.Direction||{};

this.Dir.UP = new Direction(0, -1);
this.Dir.DOWN = new Direction(0, 1);
this.Dir.LEFT = new Direction(-1, 0);
this.Dir.RIGHT = new Direction(1, 0);