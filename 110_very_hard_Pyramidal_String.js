function calculate_pyramid_levels(string_count) {
  let level = 0;
  let total_strings = 0;

  while (total_strings < string_count) {
      level++;
      total_strings += level;
  }

  return level;
}

function is_valid_pyramid(levels, element_lengths) {
  return new Set(element_lengths).size === levels && !element_lengths.includes(0);
}

function pyramidal_string(string, _type) {
  const pyramid_level = calculate_pyramid_levels(string.length);

  if (pyramid_level === 0) {
      return [];
  }

  const result = [];
  let start = 0;
  let step = 1;
  
  if (_type === "REV") {
      start = pyramid_level - 1;
      step = -1;
  }

  for (let i = 0; i < pyramid_level; i++) {
      const end = start + i + 1;
      result.push(string.substring(start, end));
      start = end - 1;
  }

  if (is_valid_pyramid(pyramid_level, result.map(s => s.length))) {
      return result.map(word => word.split('').join(' '));
  }

  return "Error!";
}

// Test cases
console.log(pyramidal_string("", "REG"));
console.log(pyramidal_string("ZAPHODBEEBLEBROX", "REG"));
// Add other test cases similarly
