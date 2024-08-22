import matplotlib.pyplot as plt
import matplotlib.animation as animation

import AnimationShapes

# update()-function to be used in FuncAnimation() in animate()
# specifies what actions to perform on the figure in between frames
def update(frame, fig, ax, shapes, customShapes):
    artists = []
    
    # clear current picture but keep x- and y-limits and background
    if customShapes != ():
        bg = fig.canvas.copy_from_bbox(ax.bbox)
        lims = [ax.get_xlim(), ax.get_ylim()]
        
        ax.clear()
        
        fig.canvas.restore_region(bg)
        ax.set_xlim(lims[0])
        ax.set_ylim(lims[1])
        
    # update positions of all shapes
    for s in shapes:
        s.updateShape(frame)
        if isinstance(s, AnimationShapes.MovingShape) and s.showTrajectory:
            if len(artists) == 0:
                artists.append(*ax.plot(s.transTraj[0][0], s.transTraj[1][0], color='b'))
            artists[0].set_data(s.transTraj[0][:frame], s.transTraj[1][:frame])
    
    # add previoulsy cleared artists back to picture with updated positions
    if customShapes != ():
        addArtists(ax, shapes, customShapes)
    
    # return all used artists (fundamental matplotlib shapes) for
    # faster rerndering using blitting (see FuncAnimation())
    for s in shapes:
        # for self-defined shapes
        if isinstance(s.shape, customShapes):
            artists.append(*s.shape.getArtists())
        # for standard matplotlib shapes
        else:
            artists.append(s.shape)
    
    return artists

def addArtists(axes, shapes, customShapes=()):
    # add shapes to ax
    for s in shapes:
        if isinstance(s.shape, customShapes):
            artists = s.shape.getArtists()
            for a in artists:
                axes.add_artist(a)
        else:
            axes.add_artist(s.shape)

# create animation
def animate(figure, axes, shapes, stepSize, customShapes=(), saveGif=False, fileName='', fps=40, dpi=100):
    addArtists(axes, shapes, customShapes)
    
    frames = range(0, len(shapes[0].trajectory), int(1/(fps*stepSize)))
    # function that creates animation on a given figure. an update()-function needs to be defined
    # that specifies what actions to perform on the figure in between frames 
    # Documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
    anim = animation.FuncAnimation(
        figure,
        update,
        frames=frames,
        fargs=(figure, axes, shapes, customShapes),
        interval=1.0/fps*1000,
        blit=True,
        repeat=True,
        save_count=30
    )

    if(saveGif):
        print("Saving")
        anim.save('./img/'+str(fileName)+'Anim.gif',
                  dpi=dpi,
                  writer=animation.PillowWriter(fps=fps),
                  progress_callback=lambda i, n: print(f'Saving frame {i} of {n}', end='\r')
                  )
        figure.savefig('./img/'+str(fileName)+'Anim.png')
    else:
        plt.show()