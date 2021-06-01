class Bounce extends Phaser.Scene {
  constructor() {
    super("Bounce");
  }

  create() {
    this.shape = this.gen_shape();
  }

  update() {
    // this.moveObjWithLimit(this.shape.rect, this.shape.velocity);
    this.gen_shape();
  }

  /* Updates the same as [moveObj]; however, if [obj] has reached the edge of 
  *  its limits, then the velocity's component changes to be in the opposite 
  *  direction. */
  moveObjWithLimit(obj, velocity) {
    if (this.shape.rect.x < this.shape.x_lt || this.shape.rect.x > this.shape.x_gt) {
      this.shape.velocity.x *= -1;
    }
    if (this.shape.rect.y < this.shape.y_lt || this.shape.rect.y > this.shape.y_gt) {
      this.shape.velocity.y *= -1;
    }
    this.moveObj(this.shape.rect, this.shape.velocity);
  }

  /* Returns a new shape object that randomly generates its size, color, 
  *  spawn position, and velocity. */
  gen_shape() {
    var width = rand_int(40, 75);
    var height = rand_int(40, 75);
    var x_lt = 0 + width / 2;
    var x_gt = screenWidth - width / 2;
    var y_lt = 0 + height / 2;
    var y_gt = screenHeight - height / 2;
    var shape = {
      "rect": this.add.rectangle(rand_int(x_lt, x_gt), rand_int(y_lt, y_gt),
        width, height, parseInt(randomColor().substring(1), 16)),
      "velocity": {
        "x": rand_int(5, 10),
        "y": rand_int(5, 10)
      },
      "x_lt": x_lt,
      "x_gt": x_gt,
      "y_lt": y_lt,
      "y_gt": y_gt
    };
    return shape;
  }

  /* Returns array of randomly generated shapes that were 
  *  generated from gen_shape. */
  gen_shapes(n) {

  }

  /* Updates the position of [obj] by [velocity]. Requires [obj] to have the 
  *  attributes x and y and [velocity] to be an Object that contains fields "x" 
  *  and "y" that both map to numbers. */
  moveObj(obj, velocity) {
    // check for precondition later
    obj.x += velocity.x;
    obj.y += velocity.y;
  }
}

function rand_int(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}