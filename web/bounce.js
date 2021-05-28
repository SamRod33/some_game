class Bounce extends Phaser.Scene {
  constructor() {
    super("Bounce");
  }

  create() {
    this.shape = {
      "rect": this.add.rectangle(screenWidth / 2, screenHeight / 2, 75, 75, 0x0000ff),
      "velocity": {
        "x": 1,
        "y": 0
      }
    };
  }

  update() {
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