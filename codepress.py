def point_in_polygon(x, y, polygon_points):
    num_points = len(polygon_points)
    inside = False
    for i in range(num_points):
        p1x, p1y = polygon_points[i]
        p2x, p2y = polygon_points[(i + 1) % num_points]
        if ((p1y > y) != (p2y > y)) and (x < (p2x - p1x) * (y - p1y) / (p2y - p1y) + p1x):
            inside = not inside
    return inside

def minimal_presses(polygon_points, brush_size):
    min_x = min(point[0] for point in polygon_points)
    max_x = max(point[0] for point in polygon_points)
    min_y = min(point[1] for point in polygon_points)
    max_y = max(point[1] for point in polygon_points)  

    covered_area = set()
    press_count = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if point_in_polygon(x, y, polygon_points):
                already_covered = False
                for dx in range(brush_size):
                    for dy in range(brush_size):
                        if (x + dx, y + dy) in covered_area:
                            already_covered = True
                            break
                    if already_covered:
                        break
                if not already_covered:
                    press_count += 1
                    for dx in range(brush_size):
                        for dy in range(brush_size):
                            covered_area.add((x + dx, y + dy))
    return press_count

def main():
    num_points = int(input())
    polygon_points = [tuple(map(int, input().split())) for _ in range(num_points)]
    brush_size = int(input())
    result = minimal_presses(polygon_points, brush_size)
    print(result, end="")

if __name__ == "__main__":
    main()
