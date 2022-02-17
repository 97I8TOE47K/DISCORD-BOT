import AxC_777_Music.main as music_nonslash
import AxC_777_Music.slash as music_slash
import AxC_777.ctx.main as gp_ctx_main
import AxC_777.non_ctx.main as gp_non_ctx_main

if __name__ == '__main__':
	music_nonslash.setup()
	music_slash.setup()
	gp_ctx_main.setup()
	gp_non_ctx_main.setup()
