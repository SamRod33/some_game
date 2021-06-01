class Bounce extends Phaser.Scene {
  constructor() {
    super("Bounce");
  }

  create() {
    this.shape = {
      "rect": this.add.rectangle(screenWidth / 2, screenHeight / 2, 75, 75, 0x0000ff),
      "velocity": {
        "x": 10,
        "y": 5
      },
      "dummy": 100,
      "x_lt": 0 + 75 / 2,
      "x_gt": screenWidth - 75 / 2,
      "y_lt": 0 + 75 / 2,
      "y_gt": screenHeight - 75 / 2
    };
  }

  update() {
    this.moveObjWithLimit(this.shape.rect, this.shape.velocity);
  }

  moveObjWithLimit(obj, velocity) {
    if (this.shape.rect.x < this.shape.x_lt || this.shape.rect.x > this.shape.x_gt) {
      this.shape.velocity.x *= -1;
    }
    if (this.shape.rect.y < this.shape.y_lt || this.shape.rect.y > this.shape.y_gt) {
      this.shape.velocity.y *= -1;
    }
    this.moveObj(this.shape.rect, this.shape.velocity);
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