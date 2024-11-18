import type { ReactElement, ReactNode } from 'react';

declare global {
  namespace React {
    interface ReactElement {
      children?: ReactNode;
    }
  }
}

declare module 'react-konva' {
  import type { ComponentType } from 'react';
  import type Konva from 'konva';

  export interface StageProps {
    width: number;
    height: number;
    onMouseDown?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    onMouseMove?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    onMouseUp?: (e: Konva.KonvaEventObject<MouseEvent>) => void;
    className?: string;
    children?: React.ReactNode;
  }

  export interface LayerProps {
    children?: React.ReactNode;
  }

  export interface LineProps {
    points: number[];
    stroke: string;
    strokeWidth: number;
    tension?: number;
    lineCap?: string;
    lineJoin?: string;
  }

  export const Stage: ComponentType<StageProps>;
  export const Layer: ComponentType<LayerProps>;
  export const Line: ComponentType<LineProps>;
}
