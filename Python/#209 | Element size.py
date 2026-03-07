#07-03-2026 | 07-03-2026

def get_element_size(window_size, element_vw, element_vh):
    window_width, window_height = map(int, window_size.split('x'))

    #replace the letters with null
    view_width = int(element_vw.replace('vw', ''))
    view_height = int(element_vh.replace('vh', ''))

    #int() is used to round the values
    pixel_width = int(view_width * window_width / 100)
    pixel_height = int(view_height * window_height / 100)

    return f'{pixel_width} x {pixel_height}'
