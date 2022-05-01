<?php

function arrayRecursiveDiff($aArray1, $aArray2) {
  $aReturn = array();

  foreach ($aArray1 as $mKey => $mValue) {
    if (array_key_exists($mKey, $aArray2)) {
      if (is_array($mValue)) {
        $aRecursiveDiff = arrayRecursiveDiff($mValue, $aArray2[$mKey]);
        if (count($aRecursiveDiff)) { $aReturn[$mKey] = $aRecursiveDiff; }
      } else {
        if ($mValue !== $aArray2[$mKey]) {
          $aReturn[$mKey] = $mValue;
        }
      }
    } else {
      $aReturn[$mKey] = $mValue;
    }
  }
  return $aReturn;
}

function assert_list ($a, $b) {
    return arrayRecursiveDiff($a, $b) === [] && arrayRecursiveDiff($b, $a) === [];
}

function assert_dict ($a, $b) {
    return arrayRecursiveDiff($a, $b) === [] && arrayRecursiveDiff($b, $a) === [];
}

function assert_float ($a, $b) {
    return gettype($a) === "double" && $a === $b;
}

function assert_str ($a, $b) {
    return gettype($a) === "string" && $a === $b;
}

function assert_none ($a, $b) {
  return $a === null && $b === null;
}
function assert_bool ($a, $b) {
  return gettype($a) == "boolean" && $a === $b;
}
function assert_int ($a, $b) {
  return gettype($a) == "integer" && $a === $b;
}

?>
