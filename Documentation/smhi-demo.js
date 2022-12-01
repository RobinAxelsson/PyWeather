/*
 This is a demo application. It uses jQuery.
 Use it on your on risk. No warranties are made.
 It is intended as a working example on how to use the API.
 */
/*
 Declaration of smhi and functions for retrieval of data in json format
 */
 (function(smhi, $, undefined) {
    // The API end points.
    smhi.baseUrl = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2";
    smhi.approvedTimeEndPoint = smhi.baseUrl + "/approvedtime.json";
    smhi.validTimeEndPoint = smhi.baseUrl + "/geotype/multipoint/validtime.json";
    smhi.parametersEndPoint = smhi.baseUrl + "/parameter.json";
    smhi.multiPointEndPoint = smhi.baseUrl + "/geotype/multipoint.json";
    smhi.forecastEndPoint = smhi.baseUrl + "/geotype/multipoint/validtime/{validtime}/parameter/{parameter}/leveltype/{leveltype}/level/{level}/data.json?with-geo=false";
    smhi.map = null;
    smhi.layer = null;
    smhi.gradientColors = ["#FF0000", "#F10D02", "#E41A04", "#D62806", "#C93508", "#BB430A", "#AE500C", "#A15D0E", "#936B10", "#867812", "#788614", "#6B9316", "#5DA118", "#50AE1A", "#43BB1C", "#35C91E", "#28D620", "#1AE422", "#0DF124", "#00FF26"];
    smhi.multiPoint = null;
    smhi.validTime = null;
    smhi.parameter = null;
    smhi.forecast = null;
    smhi.approvedTime = null;
    smhi.referenceTime = null;
    /*
    Get all the grid points - 'callback(validTime)' is called on completion. No error handling!
    */
    smhi.getApprovedTime = function(callback) {
        $.getJSON(smhi.approvedTimeEndPoint).done(function(approvedTime) {
            callback(approvedTime);
        });
    };
    /*
    Get all the grid points - 'callback(multiPoint)' is called on completion. No error handling!
    */
    smhi.getMultiPoint = function(callback) {
        $.getJSON(smhi.multiPointEndPoint).done(function(multiPoint) {
            smhi.multiPoint = multiPoint;
            callback(multiPoint);
        });
    };
    /*
    Get the latest forecast valid times - 'callback(validTime)' is called on completion. No error handling!
    */
    smhi.getValidTime = function(callback) {
        $.getJSON(smhi.validTimeEndPoint).done(function(validTime) {
            smhi.validTime = validTime;
            callback(validTime);
        });
    };
    /*
    Get the parameters for the selected valid time - 'callback(parameter)' is called on completion. No error handling!
    */
    smhi.getParameter = function(callback) {
        $.getJSON(smhi.parametersEndPoint).done(function(parameter) {
            smhi.parameter = parameter;
            callback(parameter);
        });
    };
    /*
     Get the latest forecast - 'callback(forecast)' is called on completion. No error handling!
     */
    smhi.getForecast = function(callback) {
        var endPoint = smhi.forecastEndPoint
            .replace("{validtime}", $("#valid-time-select").val().replace(/-/g, "").replace(/:/g, ""))
            .replace("{parameter}", $("#parameter-select").val().toLowerCase())
            .replace("{leveltype}", $("#level-type-select").val())
            .replace("{level}", $("#level-select").val());
        $.getJSON(endPoint).done(function(forecast) {
            smhi.forecast = forecast;
            callback(forecast);
        });
    };
}(window.smhi = window.smhi || {}, jQuery));
$(document).ready(function() {
    run_waitMe("win8");
    // create leaflet map and disable interaction
    var southWest = L.latLng(52.500440, 2.250475);
    var northEast = L.latLng(70.742227, 37.934697);
    bounds = L.latLngBounds(southWest, northEast);
    smhi.map = L.map('map', {
        crs: L.CRS.EPSG900913,
        zoomControl: false,
        minZoom: 5,
        maxZoom: 10,
        maxBounds: bounds
    }).setView([63, 17], 4);
    L.control.mousePosition().addTo(smhi.map);
    // the map layer
    var background = L.tileLayer.wms("https://opendata-view.smhi.se/wms", {
        layers: 'opendata_default_map_2',
        format: 'image/png',
        transparent: false,
        bgcolor: '#B2D0FD',
        attribution: "copyright 2014 SMHI"
    });
    smhi.map.addLayer(background);
    $("#valid-time-select").change(function() {
        changeValidTime();
    });
    $("#parameter-select").change(function() {
        changeParameter();
    });
    $("#level-type-select").change(function() {
        changeLevelType();
    });
    $("#level-select").change(function() {
        changeLevel();
    });
    reloadApprovedTime();
    // Get all the grid points
    smhi.getMultiPoint(function(multiPoint) {
        smhi.multiPoint = multiPoint;
        getValidTimes(true);
    });
    return false;
});
function getParameters() {
    $("#parameter-select").empty();
    // Get the parameters
    smhi.getParameter(function(parameter) {
        smhi.parameter = parameter;
        jQuery.each(smhi.parameter.parameter, function(index, value) {
            if ($("#parameter-select option[value='" + value.name + "']").length == 0) {
                $('#parameter-select').append($('<option>', {
                    value: value.name,
                    text: value.name
                }));
            }
        });
        $('#valid-time-select').selectpicker('refresh');
        $('#parameter-select').selectpicker('refresh');
        changeParameter();
    });
}
function getValidTimes(loadParameters) {
    // Get the valid times
    smhi.getValidTime(function(validTime) {
        var validTimes = smhi.validTime.validTime;
        jQuery.each(validTimes, function(index, value) {
            $('#valid-time-select').append($('<option>', {
                value: value,
                text: value
            }));
        });
        $('#valid-time-select').selectpicker('refresh');
        if (loadParameters) {
            getParameters();
        }
    });
}
function reloadApprovedTime() {
    // Get the approved time
    smhi.getApprovedTime(function(approvedTime) {
        if (smhi.approvedTime == null || (smhi.approvedTime != null && smhi.approvedTime != approvedTime.approvedTime)) {
            if (smhi.approvedTime != null) {
                smhi.approvedTime = approvedTime.approvedTime;
                smhi.referenceTime = approvedTime.referenceTime;
                alert("Approved time has changed from " + smhi.approvedTime + " to " + approvedTime.approvedTime + ". Reloading data!");
                getValidTimes(false);
                return false;
            } else {
                smhi.approvedTime = approvedTime.approvedTime;
                smhi.referenceTime = approvedTime.referenceTime;
            }
            $('#reference-time').html(smhi.referenceTime);
            $('#approved-time').html(smhi.approvedTime);
        }
        return true;
    });
}
function changeValidTime() {
    if (!reloadApprovedTime()) {
        getForecast();
    }
}
function changeParameter() {
    $("#level-type-select").empty();
    $("#level-select").empty();
    jQuery.each(smhi.parameter.parameter, function(index, parameter) {
        if (parameter.name == $('#parameter-select').val()) {
            if ($("#level-type-select option[value='" + parameter.levelType + "']").length == 0) {
                $('#level-type-select').append($('<option>', {
                    value: parameter.levelType,
                    text: parameter.levelType
                }));
            }
        }
    });
    $('#parameter-select').selectpicker('refresh');
    $('#level-type-select').selectpicker('refresh');
    changeLevelType();
}
function changeLevelType() {
    $("#level-select").empty();
    jQuery.each(smhi.parameter.parameter, function(index, parameter) {
        if (parameter.name == $('#parameter-select').val() &&
            parameter.levelType == $('#level-type-select').val()) {
            if ($("#level-select option[value='" + parameter.level + "']").length == 0) {
                $('#level-select').append($('<option>', {
                    value: parameter.level,
                    text: parameter.level
                }));
            }
        }
    });
    $('#level-type-select').selectpicker('refresh');
    $('#level-select').selectpicker('refresh');
    changeLevel();
}
function changeLevel() {
    console.log("Get data for " + $("#valid-time-select").val() + ", " + $("#parameter-select").val() + ", " + $("#level-type-select").val() + ", " + $("#level-select").val() + ".");
    getForecast();
}
function getForecast() {
    if ($(".waitMe").length == 0) {
        run_waitMe("win8");
    }
    if (smhi.layer != null) {
        smhi.map.removeLayer(smhi.layer);
    }
    // Get the forecast
    smhi.getForecast(function(forecast) {
        jQuery.each(smhi.forecast.timeSeries, function(index, timeSerie) {
            if ($("#valid-time-select").val() == timeSerie.validTime) {
                jQuery.each(timeSerie.parameters, function(index, parameter) {
                    if ($("#parameter-select").val() == parameter.name &&
                        $("#level-type-select").val() == parameter.levelType &&
                        $("#level-select").val() == parameter.level) {
                        if (parameter.values && parameter.values.length > 0) {
                            var maxValue = -Infinity;
                            var minValue = Infinity;
                            for (var i = 0; i < parameter.values.length; i++) {
                                if (parameter.values[i] > maxValue) {
                                    maxValue = parameter.values[i];
                                }
                                if (parameter.values[i] < minValue) {
                                    minValue = parameter.values[i];
                                }
                            }
                            var gradient = getGradientArray(minValue, maxValue);
                            var markers = [];
                            jQuery.each(parameter.values, function(index, value) {
                                if (index % 100 == 0) {
                                    var marker = L.circleMarker(
                                        [smhi.multiPoint.coordinates[index][1],
                                            smhi.multiPoint.coordinates[index][0]
                                        ],
                                        getStyle(gradient, value)).setRadius(3);
                                    marker.on('mouseover', function(e) {
                                        //open popup;
                                        var popup = L.popup({
                                                closeButton: false
                                            })
                                            .setLatLng(e.latlng)
                                            .setContent('' + value + '')
                                            .openOn(smhi.map);
                                    });
                                    markers.push(marker);
                                }
                            });
                            smhi.layer = L.featureGroup(markers).setStyle();
                            smhi.layer.addTo(smhi.map);
                            createLegend(gradient);
                        }
                    }
                });
            }
        });
        $("#demo-content").waitMe("hide");
    });
}
function getGradientArray(min, max) {
    var step = (max - min) / (smhi.gradientColors.length - 1);
    var gradient = [];
    for (var i = 0; i < smhi.gradientColors.length; i++) {
        var key = min + step * (i + 1);
        if (max + step > 1000 || min - step < -1000) {
            key = +key.toFixed(0);
        } else if (max + step > 100 || min - step < -100) {
            key = +key.toFixed(1);
        } else {
            key = +key.toFixed(2);
        }
        gradient[i] = key;
    }
    return gradient;
}
function getStyle(gradient, value) {
    var color = getColor(gradient, value);
    return {
        color: color,
        fillColor: color,
        weight: 0,
        opacity: 1,
        fillOpacity: 0.7
    };
}
function getColor(gradient, value) {
    for (var i = 0; i < gradient.length; i++) {
        if (value < gradient[i]) {
            return smhi.gradientColors[i];
        }
    }
}
function createLegend(gradient) {
    $("#metfcst-legend").empty();
    var legendMark = $('<div class="sid-metfcst-legend sid-metfcst-legend-mark"></div>');
    var height = 100 / smhi.gradientColors.length;
    for (var i = smhi.gradientColors.length - 1; i >= 0; i--) {
        var item = $('<a class="sid-metfcst-legend-mark-item" style="background-color: ' + smhi.gradientColors[i] + '; height: ' + height + '%"></a>');
        item.data('metfcst-legend', gradient[i]);
        item.attr('data-metfcst-legend', gradient[i]);
        item.addClass('sid-metfcst-legend-mark-border');
        legendMark.append(item);
    }
    $("#metfcst-legend").append(legendMark);
}
function run_waitMe(effect) {
    $('#demo-content').waitMe({
        // none, rotateplane, stretch, orbit, roundBounce, win8,
        // win8_linear, ios, facebook, rotation, timer, pulse,
        // progressBar, bouncePulse or img
        effect: effect,
        // place text under the effect (string).
        text: 'Please Wait. Loading data!',
        // background for container (string).
        bg: 'rgba(255,255,255,0.7)',
        // color for background animation and text (string).
        color: '#000',
        // change width for elem animation (string).
        sizeW: '80px',
        // change height for elem animation (string).
        sizeH: '80px',
        // url to image
        source: '../images/img.svg'
    });
}