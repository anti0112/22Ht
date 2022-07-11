# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, x: int, y: int, d, fly: bool, crawl: bool, base_speed=1):
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            base_speed *= 1.2
            if d == 'UP':
                new_y = y + base_speed
                new_x = x
            elif d == 'DOWN':
                new_y = y - base_speed
                new_x = x
            elif d == 'LEFT':
                new_y = y
                new_x = x - base_speed
            elif d == 'RIGHT':
                new_y = y
                new_x = x + base_speed
        if crawl:
            base_speed *= 0.5
            if d == 'UP':
                new_y = y + base_speed
                new_x = x
            elif d == 'DOWN':
                new_y = y - base_speed
                new_x = x
            elif d == 'LEFT':
                new_y = y
                new_x = x - base_speed
            elif d == 'RIGHT':
                new_y = y
                new_x = x + base_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

