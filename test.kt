import android.media.AudioRecord
import android.media.MediaRecorder
import android.content.Context
fun test(context: Context) {
    AudioRecord.Builder().setAudioSource(MediaRecorder.AudioSource.MIC).setContext(context)
}
