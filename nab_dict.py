class nab_dict(dict):
  def insert(self, name, grade, course):
    if not name in self:
      self[name] = []
    if not course in self[name]:
      self[name].append((course, grade))
    return self
  def merge(self, other):
    for name in other:
      if not name in self:
        self[name] = []
      for course in other[name]:
        if not course in self[name]:
          self[name].append(course)
    return self