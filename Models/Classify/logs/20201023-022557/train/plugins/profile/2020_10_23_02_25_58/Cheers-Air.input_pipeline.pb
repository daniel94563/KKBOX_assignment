	+���T@+���T@!+���T@	B� ��o�?B� ��o�?!B� ��o�?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$+���T@����x��?A�$���S@Ysh��|?�?*	      g@2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate/�$��?!?�S�F@)�MbX9�?1�u�)�YE@:Preprocessing2F
Iterator::Model�v��/�?!��L��>@)/�$��?1?�S�6@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeatL7�A`�?!h�`�|�1@)9��v���?1����,@:Preprocessing2U
Iterator::Model::ParallelMapV2���Q��?!v�)�Y7 @)���Q��?1v�)�Y7 @:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip����Mb�?!���LQ@)����Mb�?1���L@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensory�&1�|?!T�n0E@)y�&1�|?1T�n0E@:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice{�G�zt?!�Y7�"�@){�G�zt?1�Y7�"�@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap��ʡE�?!8�"�u�G@)�~j�t�h?1#�u�)��?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.1% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9C� ��o�?#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	����x��?����x��?!����x��?      ��!       "      ��!       *      ��!       2	�$���S@�$���S@!�$���S@:      ��!       B      ��!       J	sh��|?�?sh��|?�?!sh��|?�?R      ��!       Z	sh��|?�?sh��|?�?!sh��|?�?JCPU_ONLYYC� ��o�?b 