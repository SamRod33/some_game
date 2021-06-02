class Bounce extends Phaser.Scene {
  constructor() {
    super("Bounce");
  }

  create() {
    // this.shape = this.gen_shape();
    // this.shapes = this.gen_shapes(50);
  }

  update() {
    // this.moveObjWithLimit(this.shape, this.shape.velocity);
    this.gen_shape();
    // this.moveObjsWithLimit(this.shapes);
  }

  /* Updates the same as [moveObj]; however, if [obj] has reached the edge of 
  *  its limits, then the velocity's component changes to be in the opposite 
  *  direction. */
  moveObjWithLimit(obj, velocity) {
    if (obj.rect.x < obj.x_lt || obj.rect.x > obj.x_gt) {
      velocity.x *= -1;
    }
    if (obj.rect.y < obj.y_lt || obj.rect.y > obj.y_gt) {
      velocity.y *= -1;
    }
    this.moveObj(obj.rect, velocity);
  }

  moveObjsWithLimit(objs) {
    var i;
    for (i = 0; i < objs.length; i++) {
      this.moveObjWithLimit(objs[i], objs[i].velocity);
    }
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
        width, height, parseInt(randomColor({
          luminosity: 'bright'
        }).substring(1), 16)),
      "velocity": {
        "x": rand_int(7, 15),
        "y": rand_int(7, 15)
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
    var i;
    var out = [];
    for (i = 0; i < n; i++) {
      out.push(this.gen_shape());
    }
    return out;
  }

  /* Updates the position of [obj] by [velocity]. Requires [obj] to have the 
  *  attributes x and y and [velocity] to be an Object that contains fields "x" 
  *  and "y" that both map to numbers. */
  moveObj(obj, velocity) {
    // check for precondition later
    obj.x += velocity.x;
    obj.y += velocity.y;
    this.add.rectangle(obj.x, obj.y, obj.width, obj.height, obj.fillColor);
  }
}

function rand_int(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}