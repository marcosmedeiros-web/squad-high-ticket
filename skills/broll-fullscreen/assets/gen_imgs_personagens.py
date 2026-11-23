#!/usr/bin/env python3
# Gera as imagens de personagem do b-roll pelo Codex da assinatura do ChatGPT (`codex exec`, o gerador de imagem do
# ChatGPT, sem chave de API; só ferramenta grátis). As refs aprovadas que existirem vão como imagem de referência
# (`codex exec -i`). Antes, confira se a cota da assinatura tem folga. Sai 2 se alguma imagem não for gerada.
# A pasta de trabalho é $BROLL_DIR (padrão ~/videos-broll).
import os,sys,glob,shutil,subprocess,tempfile,traceback
BASE=os.path.join(os.path.expanduser(os.environ.get("BROLL_DIR","~/videos-broll")),"brolls","char")
REFS=[r for r in (f"{BASE}/refs/ref-{n}.png" for n in ("08","13","17","21")) if os.path.isfile(r)]
LOCK=("Match the squad characters from the reference images EXACTLY (same designs, same proportions; Premium 3D character render with anime-stylised proportions, matte finish, rounded volume, no ink outline and no flat blocked colour; built from genuine materials and lit as a physical object in a studio, soft key light with a clean rim and gentle falloff. Cinematic, premium): "
 "THE EXPERT = the person on camera, appearance defined at onboarding (skin, hair or bald, facial hair, build, signature outfit); "
 "THE OWNER'S AI CHARACTER = the owner's character that represents the AI, appearance defined at onboarding (hair, skin, signature accent on neck/forearms, eyes, executive outfit); "
 "THE OWNER'S MASCOT = CHIBI mascot with the owner's mascot head defined at onboarding (species, colour, face — NOT a smooth featureless ball), baby face, huge round expressive eyes, signature hands, tiny chubby child body, black hoodie with gold chain; "
 "THE OWNER'S SIDEKICK CHARACTER = a second chibi helper character, appearance defined at onboarding; "
 "Vertical 9:16 composition. Command center / navy + red & cyan neon, holographic HUD dashboards, the owner's brand logo (defined at onboarding) glowing in neon on the wall. Cinematic. ABSOLUTELY NO text, no words, no captions, no logos with letters, no watermark.")
SCENES=[
 (1,"funcionario-ia-24h","The squad working tirelessly like a 24/7 team at glowing holographic consoles: the owner's AI character operating a big dashboard, the owner's sidekick character orchestrating screens, the owner's mascot at another console, THE EXPERT at center with arms crossed, confident and proud, overseeing the operation at night."),
 (3,"agente-100pct-seu","THE EXPERT at center receiving in their hands a glowing floating cyan-gold AI core orb (sense of ownership/power); the owner's AI character presents the orb beside him; the owner's sidekick character and the owner's mascot stand proudly. Heroic possessive mood."),
 (5,"ia-trabalha-por-mim","THE EXPERT seated like a confident boss in the foreground while their AI squad works FOR him around and behind: the owner's AI character typing on glowing screens, the owner's sidekick character commanding holograms, the owner's mascot handling a panel; floating app icons (WhatsApp, Instagram, Gmail) as soft holograms."),
 (6,"agente-no-ar-em-minutos","A brand-new AI agent being 'born' from a glowing cyan-gold portal at center; the owner's sidekick character joyfully presses one single big glowing button; the owner's mascot cheers with both hands up; the owner's AI character presents the emerging agent with an open hand; THE EXPERT nods approving. Easy one-click magical vibe."),
 (27,"o-outro-caminho","Dramatic hero shot, dawn light breaking after darkness: the squad steps forward confidently toward the camera as 'the other way' / the turning point; THE EXPERT leading center, the owner's AI character at their side, the owner's sidekick character and the owner's mascot in front; behind them the command center with the owner's neon logo. Hopeful, cinematic rim light."),
]
def codex(prompt,out):
    """Codex numa pasta só da imagem, apps/plugins/busca desligados; confere o PNG e move para `out`."""
    if not shutil.which("codex"):
        print("[ERRO] codex nao instalado (instale com `npm i -g @openai/codex` e faça login na assinatura do ChatGPT); sem ele, o b-roll de personagem vira Hyperframe",flush=True); return False
    pasta=tempfile.mkdtemp(prefix="broll-char-"); nome=os.path.basename(out)
    cmd=["codex","exec","--disable","apps","--disable","plugins","-c",'web_search="disabled"',"--skip-git-repo-check","-s","workspace-write","-C",pasta]
    for r in REFS: cmd+=["-i",r]
    cmd.append(f"Gere UMA imagem com a ferramenta de geração de imagem, vertical 1024x1536"
               f"{', usando as imagens anexadas como referência dos personagens' if REFS else ''}, seguindo exatamente este briefing. "
               f"Salve como {nome} nesta pasta e diga o caminho completo.\n\n{prompt}")
    r=subprocess.run(cmd,stdin=subprocess.DEVNULL,capture_output=True,text=True)
    feito=os.path.join(pasta,nome)
    if not os.path.isfile(feito):
        pngs=sorted(glob.glob(os.path.join(pasta,"*.png"))); feito=pngs[0] if pngs else None
    if r.returncode!=0 or not feito:
        print(f"  codex rc={r.returncode}, png={'sim' if feito else 'nao'}: {(r.stderr or r.stdout)[-300:]}",flush=True); return False
    os.makedirs(os.path.dirname(out),exist_ok=True); shutil.move(feito,out); shutil.rmtree(pasta,ignore_errors=True)
    return True
def main():
    print(f"[imgs] {len(SCENES)} imagens (Codex/ChatGPT + {len(REFS)} refs)",flush=True)
    falhas=0
    for idx,label,scene in SCENES:
        out=f"{BASE}/img/img-{idx:02d}.png"
        if codex(f"{scene}\n\n{LOCK}",out):
            print(f"[{idx:02d}] OK {label} {os.path.getsize(out)//1024}KB",flush=True)
        else:
            print(f"[{idx:02d}] FALHOU {label}",flush=True); falhas+=1
    print("[imgs] FIM",flush=True)
    return 2 if falhas else 0
if __name__=="__main__":
    try: sys.exit(main())
    except Exception: traceback.print_exc(); sys.exit(1)
