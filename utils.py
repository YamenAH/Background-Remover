from backgroundremover.bg import remove
def bg_remove(src_img_path):
  def get_rand_name():
      # Creating a new file to store the processed image
      import random
      randomfile = random.randint(10000, 100000)
      return f'images/temp_{randomfile}.png'
  def remove_bg(src_img_path, out_img_path):
      # Background Removal Function
      model_choices = ["u2net", "u2net_human_seg", "u2netp"]
      f = open(src_img_path, "rb")
      data = f.read()
      img = remove(data, model_name=model_choices[0],
                  alpha_matting=True,
                  alpha_matting_foreground_threshold=220,
                  alpha_matting_background_threshold=30,
                  alpha_matting_erode_structure_size=8,
                  alpha_matting_base_size=1000)
      f.close()
      f = open(out_img_path, "wb")
      f.write(img)
      f.close()

  new_path = get_rand_name()
  remove_bg(src_img_path, new_path)
  return new_path
