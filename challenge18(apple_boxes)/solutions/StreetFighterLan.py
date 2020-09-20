def solution(k):
  yellow_boxes, red_boxes = [box for box in range(1, k+1) if box % 2], red_boxes = [box for box in range(1, k+1) if box !% 2]
  return sum(red_boxes) - sum(yellow_boxes)