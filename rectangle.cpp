class Rectangle {
    int width, height;
  public:
    void set_values (int,int);
    int area() {return width*height;}
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}

extern "C" int set_value(int a, int b) {

  Rectangle rect;
  rect.set_values (a,b);

  return rect.area();
}
