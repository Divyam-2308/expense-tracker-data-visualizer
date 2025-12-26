import 'react-native-url-polyfill/auto';
import { createClient } from '@supabase/supabase-js';
import AsyncStorage from '@react-native-async-storage/async-storage';

const SUPABASE_URL = 'https://bxsmuczpijacejmaasdx.supabase.co/';
const SUPABASE_ANON_KEY = 'sb_publishable_MgQ1lpI3dcz6j8Z8Hd5YBA_zDE0Y-sG'

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  auth: {
    storage: AsyncStorage,
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
  },
});