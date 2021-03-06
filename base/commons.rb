def assert_list(a, b)
    a == b
end

def assert_dict(a, b)
    if a != b
        return a.transform_keys(&:to_sym) == b.transform_keys(&:to_sym)
    end
    return true
end

def assert_float(a, b)
    a == b
end

def assert_str(a, b)
  a == b
end

def assert_int(a, b)
  a == b
end

def assert_none(a, b)
  a == nil && b == nil
end

def assert_bool(a, b)
 (a == false || a == true) && a == b
end
