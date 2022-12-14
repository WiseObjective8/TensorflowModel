# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: models/research/object_detection/protos/calibration.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9models/research/object_detection/protos/calibration.proto\x12\x17object_detection.protos\"\xe4\x03\n\x11\x43\x61librationConfig\x12P\n\x16\x66unction_approximation\x18\x01 \x01(\x0b\x32..object_detection.protos.FunctionApproximationH\x00\x12\x62\n class_id_function_approximations\x18\x02 \x01(\x0b\x32\x36.object_detection.protos.ClassIdFunctionApproximationsH\x00\x12J\n\x13sigmoid_calibration\x18\x03 \x01(\x0b\x32+.object_detection.protos.SigmoidCalibrationH\x00\x12\\\n\x1d\x63lass_id_sigmoid_calibrations\x18\x04 \x01(\x0b\x32\x33.object_detection.protos.ClassIdSigmoidCalibrationsH\x00\x12\x61\n\x1ftemperature_scaling_calibration\x18\x05 \x01(\x0b\x32\x36.object_detection.protos.TemperatureScalingCalibrationH\x00\x42\x0c\n\ncalibrator\"L\n\x15\x46unctionApproximation\x12\x33\n\tx_y_pairs\x18\x01 \x01(\x0b\x32 .object_detection.protos.XYPairs\"\xe9\x01\n\x1d\x43lassIdFunctionApproximations\x12l\n\x15\x63lass_id_xy_pairs_map\x18\x01 \x03(\x0b\x32M.object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry\x1aZ\n\x16\x43lassIdXyPairsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .object_detection.protos.XYPairs:\x02\x38\x01\"\\\n\x12SigmoidCalibration\x12\x46\n\x12sigmoid_parameters\x18\x01 \x01(\x0b\x32*.object_detection.protos.SigmoidParameters\"\x8b\x02\n\x1a\x43lassIdSigmoidCalibrations\x12}\n\x1f\x63lass_id_sigmoid_parameters_map\x18\x01 \x03(\x0b\x32T.object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry\x1an\n ClassIdSigmoidParametersMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.object_detection.protos.SigmoidParameters:\x02\x38\x01\"/\n\x1dTemperatureScalingCalibration\x12\x0e\n\x06scaler\x18\x01 \x01(\x02\"\xab\x01\n\x07XYPairs\x12\x39\n\x08x_y_pair\x18\x01 \x03(\x0b\x32\'.object_detection.protos.XYPairs.XYPair\x12\x45\n\x12training_data_type\x18\x02 \x01(\x0e\x32).object_detection.protos.TrainingDataType\x1a\x1e\n\x06XYPair\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"0\n\x11SigmoidParameters\x12\r\n\x01\x61\x18\x01 \x01(\x02:\x02-1\x12\x0c\n\x01\x62\x18\x02 \x01(\x02:\x01\x30*N\n\x10TrainingDataType\x12\x15\n\x11\x44\x41TA_TYPE_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41LL_CLASSES\x10\x01\x12\x12\n\x0e\x43LASS_SPECIFIC\x10\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'models.research.object_detection.protos.calibration_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY._options = None
  _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY._serialized_options = b'8\001'
  _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY._options = None
  _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY._serialized_options = b'8\001'
  _TRAININGDATATYPE._serialized_start=1524
  _TRAININGDATATYPE._serialized_end=1602
  _CALIBRATIONCONFIG._serialized_start=87
  _CALIBRATIONCONFIG._serialized_end=571
  _FUNCTIONAPPROXIMATION._serialized_start=573
  _FUNCTIONAPPROXIMATION._serialized_end=649
  _CLASSIDFUNCTIONAPPROXIMATIONS._serialized_start=652
  _CLASSIDFUNCTIONAPPROXIMATIONS._serialized_end=885
  _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY._serialized_start=795
  _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY._serialized_end=885
  _SIGMOIDCALIBRATION._serialized_start=887
  _SIGMOIDCALIBRATION._serialized_end=979
  _CLASSIDSIGMOIDCALIBRATIONS._serialized_start=982
  _CLASSIDSIGMOIDCALIBRATIONS._serialized_end=1249
  _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY._serialized_start=1139
  _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY._serialized_end=1249
  _TEMPERATURESCALINGCALIBRATION._serialized_start=1251
  _TEMPERATURESCALINGCALIBRATION._serialized_end=1298
  _XYPAIRS._serialized_start=1301
  _XYPAIRS._serialized_end=1472
  _XYPAIRS_XYPAIR._serialized_start=1442
  _XYPAIRS_XYPAIR._serialized_end=1472
  _SIGMOIDPARAMETERS._serialized_start=1474
  _SIGMOIDPARAMETERS._serialized_end=1522
# @@protoc_insertion_point(module_scope)
