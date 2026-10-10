with open('app/src/main/java/com/example/service/BackgroundAudioService.kt', 'r') as f:
    content = f.read()

imports = """import com.example.data.DatabaseProvider
import com.example.data.LogEntry
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.CoroutineScope"""
content = content.replace('import android.util.Log', 'import android.util.Log\n' + imports)

# Where battery is connected
battery_conn = """                Intent.ACTION_POWER_CONNECTED -> {
                    if (isTtsInitialized) {
                        tts?.speak("ira charging connect janu", TextToSpeech.QUEUE_FLUSH, null, "ChargeConnected")
                    }
                    CoroutineScope(Dispatchers.IO).launch {
                        val db = DatabaseProvider.getDatabase(context)
                        db.logDao().insertLog(LogEntry(type = "BATTERY", message = "Charging Connected"))
                    }
                }"""
content = content.replace(
    '''                Intent.ACTION_POWER_CONNECTED -> {
                    if (isTtsInitialized) {
                        tts?.speak("ira charging connect janu", TextToSpeech.QUEUE_FLUSH, null, "ChargeConnected")
                    }
                }''', battery_conn
)

# Where charge is full
charge_full = """                            if (isTtsInitialized) {
                                tts?.speak("charge full hogaya he", TextToSpeech.QUEUE_FLUSH, null, "ChargeFull")
                            }
                            CoroutineScope(Dispatchers.IO).launch {
                                val db = DatabaseProvider.getDatabase(context)
                                db.logDao().insertLog(LogEntry(type = "BATTERY", message = "Battery Fully Charged"))
                            }"""
content = content.replace(
    '''                            if (isTtsInitialized) {
                                tts?.speak("charge full hogaya he", TextToSpeech.QUEUE_FLUSH, null, "ChargeFull")
                            }''', charge_full
)

with open('app/src/main/java/com/example/service/BackgroundAudioService.kt', 'w') as f:
    f.write(content)
